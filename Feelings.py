class Feeling:
    def _init_(self, situation, intensity=1, negativeMeter=100):
        self._situation = situation
        self._intensity = intensity
        self._negativeMeter = negativeMeter
        self._heartbeat = 70  # default resting heartbeat

    #initial methods
    def describe(self):
        pass
    
    def physicalResponse(self):
        pass
    
    def timePasses(self, days):
        pass

    def response(self, event):
        pass

    def influenceByEnv(self, environment):
        pass

#getters and setters
    def getSituation(self):
        return self._situation
    
    def setSituation(self, situation):
        self._situation = situation

    def getIntensity(self):
        return self._intensity

    def setIntensity(self, intensity):
        self._intensity = intensity

    def getNegativeMeter(self):
        return self._negativeMeter

    def setNegativeMeter(self, negativeMeter):
        self._negativeMeter = negativeMeter

    def getHeartbeat(self):
        return self._heartbeat

    def setHeartbeat(self, heartbeat):
        self._heartbeat = heartbeat
