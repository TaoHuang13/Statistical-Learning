import numpy as np
from functools import reduce

class perceptron(object):
    def __init__(self, lr):
        self.lr = lr

    def train(self, feature, label, dual = False):
        # 获取数据信息
        m, n = feature.shape        

        # 非对偶
        if !dual:
            self.w, self.b = np.random.random(n), np.random.random(1)

            # 采用顺序遍历
            while True:
                error_count = 0
                for i in range(m):
                    dist = label[i] * np.dot(self.w, feature[i] + self.b)
                    
                    # 如果dist<0,则需要更新
                    if dist <= 0:
                        error_count += 1
                        self.w += self.lr * label[i] * feature[i]
                        self.b += self.lr * label[i]
                
                if error_count == 0:
                    break

        # 对偶
        else:
            Gram = np,array([[np.dot(feature[i], feature[j]) for j in range(m)] for i in range(m)])
            self.alpha, self.b = np.zeros(m), np.random.random(1)

            while True:
                error_count = 0
                for i in range(m):
                    dist = reduce(lambda x, y: x + y, self.alpha * label * Gram[i])

                    if dist <= 0:
                        error_count += 1
                        self.alpha += self.lr
                        self.b += self.lr * label[i]

                if error_count == 0:
                    break
            
            self.w = np.matmul(self.alpha * label, feature)

    def predict(self, feature):
        dist = np.dot(self.w, feature[i] + self.b)
        return 1 if dist > 0 else 0
        
