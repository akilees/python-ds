
class LogicGates:

    def __init__(self, n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output


class BinaryGate(LogicGates):

    def __init__(self, n):
        LogicGates.__init__(self, n)

        self.pinA = None
        self.pinB = None

    def setNextPin(self, source):

        if self.pinA == None:
            self.pinA = source
        elif self.pinB == None:
            self.pinB = source
        else:
            print("cannot connect: no empty pins on this gate")

    def getPinA(self):
        # why not assign pinA here??
        if self.pinA is None:
            return int(input("Enter Pin A input for gate " + self.getLabel() + "---> "))
        else:
            # why can pinA call getFrom()? isn't it a method for Connector object?
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB is None:
            return int(input("Enter Pin B input for gate " + self.getLabel() + "---> "))
        else:
            return self.pinB.getFrom().getOutput()


class UnaryGate(LogicGates):

    def __init__(self, n):
        LogicGates.__init__(self, n)

        self.pin = None

    def getPin(self):
        if self.pin is None:
            return int(input("Enter Pinde input for gate " + self.getLabel() + "---> "))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self, source):

        if self.pin == None:
            self.pin = source
        else:
            print("cannot connect: no empty pins on this gate")


class AndGate(BinaryGate):

    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):

        # how do you return when pin not assigned...
        # return self.pinA and self.pinB

        a = self.getPinA()
        b = self.getPinB()

        if a == 1 and b == 1:
            return 1
        else:
            return 0


class OrGate(BinaryGate):

    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()

        if a == 0 and b == 0:
            return 0
        else:
            return 1


class NotGate(UnaryGate):

    def __init__(self, n):
        UnaryGate.__init__(self, n)

    def performGateLogic(self):

        p = self.getPin()

        if p == 1:
            return 0
        else:
            return 1


class Connector:

    def __init__(self, fgate, tgate):

        # why assign to a new variable fromgate, why not just use fgate as is?
        self.fromgate = fgate
        self.togate = tgate

        ## TODO: why????? wrote 128, but 129 is text book
        # self.togate.setNextPin(self.fromgate)
        tgate.setNextPin(self)

    # had trouble in this function, what to do, what to put in init, where to put connection logic
    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate


if __name__ == '__main__':
    # test_gate = AndGate("test and gate")
    # test_gate.getLabel()
    # print(test_gate.getOutput())
    #
    # g2 = OrGate("G2")
    # print(g2.getLabel())
    # print(g2.getOutput())
    #
    # g3 = NotGate("N3")
    # print(g3.getLabel())
    # print(g3.getOutput())

    g1 = AndGate("G1")
    g2 = AndGate("G2")
    g3 = OrGate("G3")
    g4 = NotGate("G4")
    c1 = Connector(g1, g3)
    c2 = Connector(g2, g3)
    c3 = Connector(g3, g4)
    print(g4.getOutput())
