import  LinRegLearner,BagLearner
class InsaneLearner(object):
    def __init__(self, bag_learner=BagLearner.BagLearner, linear_learner=LinRegLearner.LinRegLearner, verbose=False):
        self.bag_learners = [bag_learner(learner=linear_learner, bags=20) for i in range(20)]
    def add_evidence(self, dataX, dataY):
        for bag_learner in self.bag_learners: bag_learner.add_evidence(dataX, dataY)
    def query(self, points): return  sum([learner.query(points) for learner in self.bag_learners])/len([learner.query(points) for learner in self.bag_learners])
    def author(self): return ""
