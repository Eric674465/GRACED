class ApplicatNode:
    def __init__(self, student_id, name, program, score):
        self.student_id = student_id
        self.name = name
        self.program = program
        self.score = score
        self.next = None

class Appplicatonlist:
    def __init__(self):
        self.head = None

    def add_application(self, student_id, name, program, score):
        new_applicant = ApplicatNode(student_id, name, program, score)

        if not self.head:
            self.head = new_applicant
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_applicant

    def display_applications(self):
        current = self.head
        while current:
            print(f"ID: {current.student_id}, Name: {current.name}, Program: {current.program}, Score: {current.score}")
            current = current.next
    
    def to_list_of_tuples(self):
        applicant_list = []
        current = self.head
        while current:
            applicant_list.append((current.student_id, current.name, current.program, current.score))
            current = current.next
        return applicant_list
    

class Waitlistqueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, applicant):  # Corrected: enqueue takes an applicant
        self.queue.append(applicant)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    def is_empty(self):
        return len(self.queue) == 0

    def display_waitlist(self):
        if self.is_empty():
            print("Waitlist is empty.")
        else:
            for applicant in self.queue:
                print(f"ID: {applicant[0]}, Name: {applicant[1]}, Program: {applicant[2]}, Score: {applicant[3]}")

class RejectedStack:
    def __init__(self):
        self.stack = []

    def push(self, applicant, reason=""):
        self.stack.append((applicant, reason))


    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def is_empty(self):
        return len(self.stack) == 0

    def display_rejected(self):
        print("Rejected Applications:")
        if self.is_empty():
            print("Rejected list is Empty") # fixed typo here
        else:
            for applicant, reason in reversed(self.stack):
                print(f"ID: {applicant[0]}, Name: {applicant[1]}, Program: {applicant[2]}, Score: {applicant[3]}, reason: {reason}")


class BSTNode:
    def __init__(self, student_id, name, program, score):
        self.student_id = student_id
        self.name = name
        self.program = program
        self.score = score
        self.left = None
        self.right = None

class AcceptedTree:
    def __init__(self):
        self.root = None

    def delete(self, student_id, node=None):  # Question 22
        if node is None:
            node = self.root

        if node is None:
            return None  # Not found

        if student_id < node.student_id:
            node.left = self.delete(student_id, node.left)
        elif student_id > node.student_id:
            node.right = self.delete(student_id, node.right)
        else:  # Found the node to delete
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:  # Node with two children
                min_right = self._find_min(node.right)
                node.student_id = min_right.student_id
                node.name = min_right.name
                node.program = min_right.program
                node.score = min_right.score
                node.right = self.delete(min_right.student_id, node.right)  # Delete the inorder successor
        return node
    
    def insert_by_name(self, student_id, name, program, score):  # Corrected: Only one definition
        if not self.root:
            self.root = BSTNode(student_id, name, program, score)
        else:
            self._insert_by_name(self.root, student_id, name, program, score)

    def _insert_by_name(self, node, student_id, name, program, score):  # Corrected logic
        if name < node.name:  # Compare names for name-based insertion
            if node.left:
                self._insert_by_name(node.left, student_id, name, program, score)
            else:
                node.left = BSTNode(student_id, name, program, score)
        else:  # Go right if name is greater or equal
            if node.right:
                self._insert_by_name(node.right, student_id, name, program, score)
            else:
                node.right = BSTNode(student_id, name, program, score)
    
    def find_highest_score(self):  # Question 24
        if not self.root:
            return None
        
        current =self.root
        while current.right:  # Traverse to the rightmost node
            current = current.right
        return current

    def to_sorted_linked_list(self): # Question 25
        nodes = []
        self._inorder_nodes(self.root, nodes)  # Inorder traversal to get sorted nodes
        if not nodes:
            return None  # Handle empty tree case

        head = ApplicatNode(nodes[0].student_id, nodes[0].name, nodes[0].program, nodes[0].score) # Create the head
        current = head
        for node in nodes[1:]: # Create other nodes and link them
            new_node = ApplicatNode(node.student_id, node.name, node.program, node.score)
            current.next = new_node
            current = new_node
        return head

    def _inorder_nodes(self, node, nodes):
        if node:
            self._inorder_nodes(node.left, nodes)
            nodes.append(node)
            self._inorder_nodes(node.right, nodes)



    def in_order_traversal(self, node=None):
        if node is None:
            node = self.root
        if node:  # Check if node is not None
            if node.left:
                self.in_order_traversal(node.left)
            print(f"ID: {node.student_id}, Name: {node.name}, Program: {node.program}, Score: {node.score}")
            if node.right:
                self.in_order_traversal(node.right)

class AdmissionSystem:
    def __init__(self):
        self.applications = Appplicatonlist()
        self.accepted = AcceptedTree()
        self.waitlist = Waitlistqueue()
        self.rejected = RejectedStack()
        self.program_capacity = {"Computer Science": 2, "Engineering": 2}

    def  reverse_waitlist(self):  # Question 17
        temp_stack = RejectedStack()  # Reuse the stack implementation
        while not self.waitlist.is_empty():
            applicant = self.waitlist.dequeue()
            temp_stack.push(applicant)

        while not temp_stack.is_empty():
            applicant = temp_stack.pop()
            self.waitlist.enqueue(applicant)

    def help_desk_simulation(self):  # Question 18
        while not self.waitlist.is_empty():
            applicant = self.waitlist.dequeue()
            print(f"Serving applicant: ID: {applicant[0]}, Name: {applicant[1]}") # Simulate serving the applicant

    def prioritize_waitlist(self):  # Question 19
        self.waitlist.queue.sort(key=lambda x: x[3], reverse=True)  # Sort by score (descending)


    def submit_application(self, student_id, name, program, score):
        self.applications.add_application(student_id, name, program, score)

    def process_applications(self):
        print("Entering process_applications()")
        current = self.applications.head
        while current:
           print(f"Processing applicant: {current.student_id}") 
           if self.program_capacity.get(current.program, 0) > 0:  # Use .get() and handle missing keys
              if current.program == "Computer Science" and current.score >= 70:
                self.accepted.insert_by_name(current.student_id, current.name, current.program, current.score)  # Corrected insert call
                self.program_capacity[current.program] -= 1
              elif current.program == "Engineering" and current.score >= 60:
                self.accepted.insert_by_name(current.student_id, current.name, current.program, current.score)  # Corrected insert call
                self.program_capacity[current.program] -= 1
              else:
                self.rejected.push((current.student_id, current.name, current.program, current.score))
        else:
            self.waitlist.enqueue((current.student_id, current.name, current.program, current.score))

        current = current.next  # Move to the next application  <-- CORRECTED: No change needed here logically

    def find_common_applicants(self, program1, program2):  # Question 8
        program1_applicants = set()
        program2_applicants = set()

        current = self.applications.head
        while current:
            if current.program == program1:
                program1_applicants.add((current.student_id, current.program))
            elif current.program == program2:
                program2_applicants.add((current.student_id, current.program))
            current = current.next  # Move to the next application (outside the loop)

        common_applicants = program1_applicants.intersection(program2_applicants)
        return common_applicants

    def extract_program_applicants(self, program_name):  # Question 13 (Only one definition)
        applicant_tuples = self.applications.to_list_of_tuples()
        program_applicants = [name for student_id, name, program, score in applicant_tuples if program == program_name]
        return program_applicants

    def is_accepted(self, applicant_tuple):  # Question 14 (Only one definition)
        student_id, name, program, score = applicant_tuple
        if program == "Computer Science" and score >= 70:
            return True
        elif program == "Engineering" and score >= 60:
            return True
        else:
            return False

    def top_3_scores(self, scores):  # Question 15
        sorted_scores = sorted(scores, reverse=True)
        return sorted_scores[:3]



    def extract_program_applicants(self, program_name): # Question 13
        applicant_tuples = self.applications.to_list_of_tuples()
        program_applicants = [name for student_id, name, program, score in applicant_tuples if program == program_name]
        return program_applicants

    def is_accepted(self, applicant_tuple): # Question 14
        student_id, name, program, score = applicant_tuple
        if program == "Computer Science" and score >= 70:
            return True  # Or set admission_status in the node
        elif program == "Engineering" and score >= 60:
            return True
        else:
            return False



    def display_all(self):
        print("\n--- Applications ---")
        self.applications.display_applications()

        print("\n--- Accepted Applicants ---")
        self.accepted.in_order_traversal()

        print("\n--- Waitlist ---")
        self.waitlist.display_waitlist()

        print("\n--- Rejected Applications ---")
        self.rejected.display_rejected()


if __name__ == "__main__":
    system = AdmissionSystem()

    system.submit_application("UG001", "Kofi Mensah", "Computer Science", 85)
    system.submit_application("UG002", "Ama Asantewaa", "Engineering", 72)
    system.submit_application("UG003", "Yaw Ofori", "Computer Science", 68)
    system.submit_application("UG004", "Abena Owusu", "Engineering", 90)
    system.submit_application("UG005", "Kwame Boateng", "Engineering", 65)
    system.submit_application("UG005", "Kwame Boateng", "Engineering", 65)
    system.submit_application("UG006", "Jane Doe", "Computer Science", 75)
    system.submit_application("UG007", "John Smith", "Engineering", 80)
    system.submit_application("UG008", "Alice", "Computer Science", 78)
    system.submit_application("UG009", "Bob", "Computer Science", 85)
    system.submit_application("UG010", "Charlie", "Engineering", 72)
    system.submit_application("UG011", "David", "Computer Science", 68)
    system.submit_application("UG012", "Eve", "Engineering", 90)
    system.submit_application("UG012", "Eugenia", "Engineering", 85)
    system.submit_application("UG012", "Bondzie", "Computer Science", 72)
    system.submit_application("UG012", "Gabriel", "Engineering", 88)
    system.submit_application("UG012", "Asimate", "Computer Science", 89)
    system.submit_application("UG012", "Julius", "Engineering", 90)
    system.submit_application("UG012", "Asiwome", "Computer Science", 74)

    system.process_applications() # crucial: process applications before displaying

    system.display_all()


     # Question 12: List of tuples
    applicant_list = system.applications.to_list_of_tuples()
    print("\nList of Applicant Tuples (ID, Name, Program, Score):")
    print(applicant_list)

    # Question 13: Applicants for a program
    cs_applicants = system.extract_program_applicants("Computer Science")
    print("\nApplicants for Computer Science:")
    print(cs_applicants)

    # Question 14: Check acceptance
    applicant_tuple = ("UG008", "Alice", "Computer Science", 78)  # Example
    is_accepted = system.is_accepted(applicant_tuple)
    print(f"\nApplicant {applicant_tuple[1]} is accepted: {is_accepted}")

    # Question 15: Top 3 scores
    scores = [85, 72, 68, 90, 65, 75, 80, 95, 60, 70]
    top_3 = system.top_3_scores(scores)
    print(f"\nTop 3 scores: {top_3}")

     # Question 17: Reverse waitlist
    system.reverse_waitlist()
    print("\nReversed Waitlist:")
    system.waitlist.display_waitlist()

    # Question 18: Help desk simulation
    print("\nHelp Desk Simulation:")
    system.help_desk_simulation()

    # Question 19: Prioritize waitlist
    system.prioritize_waitlist()
    print("\nPrioritized Waitlist:")
    system.waitlist.display_waitlist()

    # Question 20: Rejected with reasons
    system.rejected.push(("UG009", "Bob", "Engineering", 55), "Low score")
    system.rejected.display_rejected()

    # Question 22: Delete from BST
    system.accepted.delete("UG002")
    print("\nAccepted after deletion:")
    system.accepted.in_order_traversal()

    # Question 23: BST by name
    system.accepted.insert_by_name("UG010", "Charlie", "Computer Science", 92)
    print("\nAccepted BST by name:")
    system.accepted.in_order_traversal()

    # Question 24: Highest score
    highest = system.accepted.find_highest_score()
    if highest:
        print(f"\nHighest score: {highest.score} by {highest.name}")

    


  
     