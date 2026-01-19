class ParticipationQueue(Student):

    even_students = []
    odd_students = []

    def apply_rule(self):
        num = self.queue_logic()   # call parent method

        if num % 2 == 0:
            ParticipationQueue.even_students.append(self.studentid)
        else:
            ParticipationQueue.odd_students.append(self.studentid)

