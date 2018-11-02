import sys
sys.path.insert(0,'/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages')
import torch
import torch.nn as nn
from sklearn import svm
from sklearn.neural_network import MLPClassifier
import torch.nn.functional as F
import numpy as np
import pickle
import time
from torch import optim
import math
from torch.utils.data import TensorDataset,DataLoader
from torch.autograd import Variable
import random
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix

#not sure
#build SVM class
class svm(nn.Module):
    #rbf kernel
    def __init__(self):
        super(svm,self).__init__()
        #4112,6
        self.fc1 = nn.Linear(316,6)

    def forward(self,x):
        x = self.fc1(x)
        return x
    def name(self):
        return "svm"

class MLPNet(nn.Module):
    def __init__(self):
        super(MLPNet, self).__init__()
        self.fc1 = nn.Linear(316, 100)
        self.fc2 = nn.Linear(100, 6)
    def forward(self, x):
        #x = x.view(-1, 28*28)
        x = self.fc1(x)
        x = F.relu(x)
        x = self.fc2(x)

        return x

    def name(self):
        return "MLP"


class mlp(nn.Module):
    def __init__(self):
        super(mlp, self).__init__()
        self.fc1 = nn.Linear(21, 10)
        self.fc2 = nn.Linear(10, 2)
    def forward(self, x):
        #x = x.view(-1, 28*28)
        x = self.fc1(x)
        x = F.relu(x)
        x = self.fc2(x)

        return x

    def name(self):
        return "mlp"

# add MLP + SVM in nn below

class Multitask(nn.Module):
    def __init__(self, xy_x_svm,xy_y_svm, xy_x_mlp,xy_y_mlp):
        super(Multitask, self).__init__()
        #models
        self.mlp = mlp()
        self.svm = MLPNet()

    #for each item in input dataset
    #run it under 2 models (mlp,svm)

    def forward(self,xy_x_mlp, xy_x_svm):
        y_pred_mlp = self.mlp(xy_x_mlp)
        y_pred_svm = self.svm(xy_x_svm)
        return y_pred_mlp,y_pred_svm

    def name(self):
        return "Mmultitask"


#data extraction
xy_x_svm = np.loadtxt('final_sen_text_new.txt')
xy_y_svm = np.loadtxt('final_clf.txt')
#1023*21
x_data_svm = Variable(torch.from_numpy(xy_x_svm[:,0:]))
#1023*1
y_data_svm = Variable(torch.from_numpy(xy_y_svm[0:]))


xy_x_mlp = np.loadtxt('bisen_text_new.txt')
xy_y_mlp = np.loadtxt('biclf.txt')
#523*4112
x_data_mlp = Variable(torch.from_numpy(xy_x_mlp[:,0:]))
#523*1
y_data_mlp = Variable(torch.from_numpy(xy_y_mlp[0:]))

random.seed(5)

model = Multitask(x_data_svm,y_data_svm,x_data_mlp,y_data_mlp)
#model = svm()
#optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.9)
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
criterion = nn.CrossEntropyLoss()

cm = 0
for epoch in range(48):
    ave_loss = 0
    batch_idx = 0

    for batch in range(500):
        ranhi_mlp = random.randint(500,1024)
        ranlow_mlp = ranhi_mlp - 500

        ranhi_svm = random.randint(500,534)
        ranlow_svm = ranhi_svm - 500

        optimizer.zero_grad()

        x_svm, target_svm = x_data_svm[ranlow_svm:ranhi_svm], y_data_svm[ranlow_svm:ranhi_svm]
        x_mlp, target_mlp = x_data_mlp[ranlow_mlp:ranhi_mlp], y_data_mlp[ranlow_mlp:ranhi_mlp]

        out_mlp,out_svm = model(x_mlp.float(),x_svm.float())
        #out_svm = model(x_svm.float())

        loss_mlp = criterion(out_mlp, target_mlp.long())

        # edited loss_mlp.backward(retain_graph=True)

        # edited optimizer.step()

        # edited optimizer1.zero_grad()

        loss_svm = criterion(out_svm, target_svm.long())
        #total_loss = loss_mlp * 0.1 + loss_svm
        #total_loss = loss_mlp * 1.5 +loss_svm
        total_loss = loss_mlp * 0.2 + loss_svm
        #ave_loss = ave_loss * 0.9 + loss_svm.data[0] * 0.1
        ave_loss = ave_loss * 0.9 + total_loss.data[0] * 0.1


        #loss_svm.backward()
        total_loss.backward()

        optimizer.step()
        #print(batch_idx)
        if (batch_idx+1) % 100 == 0 or (batch_idx+1) == 500:
            print('==>>> epoch: {}, batch index: {}, train loss svm: {:.6f}'.format(
                epoch, batch_idx+1, ave_loss))
        batch_idx += 1



###################### testing ######################

    correct_cnt_mlp, ave_loss,correct_cnt_svm= 0, 0,0
    total_cnt_svm,total_cnt_mlp = 0,0

    batch_idx = 0

    for batch in range(100):
        ranhi = random.randint(100,523)
        ranlow = ranhi - 100

        x_svm, target_svm = x_data_svm[ranlow:ranhi], y_data_svm[ranlow:ranhi]
        x_mlp, target_mlp = x_data_mlp[ranlow:ranhi], y_data_mlp[ranlow:ranhi]

        #load model
        out_mlp,out_svm = model(x_mlp.float(),x_svm.float())
        loss_mlp = criterion(out_mlp, target_mlp.long())
        loss_svm = criterion(out_svm, target_svm.long())

        _, pred_label_mlp = torch.max(out_mlp.data, 1)
        _, pred_label_svm = torch.max(out_svm.data, 1)
        target_mlp.data = target_mlp.data.long()
        target_svm.data = target_svm.data.long()
        #print((pred_label == target.data.long()).sum())

        #exit()
        total_cnt_mlp += x_mlp.data.size()[0]
        total_cnt_svm += x_svm.data.size()[0]

        correct_cnt_mlp += (pred_label_mlp == target_mlp.data).sum()
        correct_cnt_svm += (pred_label_svm == target_svm.data).sum()

        if(batch_idx+1) % 100 == 0 or (batch_idx+1) == 100:
            print( '==>>> epoch: {}, batch index: {}, acc_mlp: {:.3f}, acc_svm: {:.3f}'.format(
                epoch, batch_idx+1, correct_cnt_mlp * 1.0 / total_cnt_mlp,correct_cnt_svm * 1.0 / total_cnt_svm))


        batch_idx += 1


    if epoch > 37:
#np.savetxt('classified_biclf.txt',tensor2numpy)
        f1_mlp = f1_score(target_mlp.data,pred_label_mlp,average='weighted')
        f1_svm = f1_score(target_svm.data,pred_label_svm,average='weighted')
        if epoch == 47:
            print('final mlp f1 score',f1_mlp)
            print('final svm f1 score',f1_svm)
        #print(confusion_matrix(target_mlp.data,pred_label_mlp))
        cm = confusion_matrix(target_svm.data,pred_label_svm) + cm

print(cm)
torch.save(model.state_dict(), model.name())
