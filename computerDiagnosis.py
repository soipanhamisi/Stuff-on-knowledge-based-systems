from experta import *
import tkinter as tk
from tkinter import scrolledtext

class ComputerTroubleshooting(KnowledgeEngine):
    def __init__(self):
        # Initialization of the parent class is performed.
        super().__init__()
        # A dictionary is created to hold scores for each identified problem.
        self.problem_scores = {}
        # A dictionary is created to hold remedies corresponding to each problem.
        self.remedies = {}

    def output(self, problem, remedy):
        # The score for the specified problem is incremented.
        if problem in self.problem_scores:
            self.problem_scores[problem] += 1
        else:
            # The problem is added to the score dictionary with an initial score.
            self.problem_scores[problem] = 1
            # The remedy for the problem is stored in the remedies dictionary.
            self.remedies[problem] = remedy

    @Rule(Fact(symptom='Slow Startup'))
    @Rule(Fact(symptom='High CPU Usage'))
    @Rule(Fact(symptom='High Memory Usage'))
    def too_many_startup_programs(self):
        # The output method is called to record the problem and its remedy.
        self.output("Too many startup programs", "Disable unnecessary startup applications")

    @Rule(Fact(symptom='Slow Application Performance'))
    @Rule(Fact(symptom='High CPU Usage'))
    def resource_intensive_app(self):
        # The output method is called to record the problem and its remedies.
        self.output("Resource-intensive application", "Close unnecessary programs")
        self.output("Resource-intensive application", "Check for updates")

    @Rule(Fact(symptom='Slow Application Performance'))
    @Rule(Fact(symptom='High Memory Usage'))
    def insufficient_ram(self):
        # The output method is called to record the problem and its remedies.
        self.output("Insufficient RAM", "Close unnecessary programs")
        self.output("Insufficient RAM", "Consider adding more RAM")

    @Rule(Fact(symptom='Slow Internet Browsing'))
    def network_browser_issue(self):
        # The output method is called to record the problem and its remedies.
        self.output("Network/Browser issue", "Check internet connection")
        self.output("Network/Browser issue", "Clear browser cache and cookies")
        self.output("Network/Browser issue", "Try a different browser")

    @Rule(Fact(symptom='Disk Space Low'))
    def full_hard_drive(self):
        # The output method is called to record the problem and its remedies.
        self.output("Full Hard Drive", "Delete unnecessary files")
        self.output("Full Hard Drive", "Uninstall unused programs")

    @Rule(Fact(symptom='Slow Computer'))
    @Rule(Fact(symptom='Outdated Drivers'))
    def outdated_drivers(self):
        # The output method is called to record the problem and its remedy.
        self.output("Outdated drivers", "Update drivers for graphics card, network adapter, etc.")

    @Rule(Fact(symptom='Slow Computer'))
    @Rule(Fact(symptom='Malware suspected'))
    def malware_infection(self):
        # The output method is called to record the problem and its remedy.
        self.output("Malware infection", "Run a full system scan with an antivirus program")

    @Rule(Fact(symptom='Slow Computer'))
    @Rule(Fact(symptom='High CPU Usage'))
    @Rule(Fact(symptom='Many Background Processes'))
    def too_many_background_processes(self):
        # The output method is called to record the problem and its remedy.
        self.output("Too many background processes", "Close unnecessary background programs")

    @Rule(Fact(symptom='Slow Computer'))
    @Rule(Fact(symptom='Hard Drive Issues suspected'))
    def hard_drive_problems(self):
        # The output method is called to record the problem and its remedies.
        self.output("Hard drive problems", "Run disk check utility")
        self.output("Hard drive problems", "Back up data")
        self.output("Hard drive problems", "Consider replacing the hard drive")

    @Rule(
        Fact(symptom='Slow Computer'),
        NOT(Fact(problem=W())),  # This rule is triggered only if no problems have been identified.
        salience=-1  # This rule is given the lowest priority.
    )
    def general_performance_issue(self):
        # The output method is called to record the problem and its remedies.
        self.output("General performance issue", "Restart the computer")
        self.output("General performance issue", "Check for updates")
        self.output("General performance issue", "Consider a system tune-up")

engine = ComputerTroubleshooting()

def diagnose():
    # Input symptoms are normalized to title case and split into a list.
    symptoms = [s.strip().title() for s in symptom_entry.get().split(",")]
    
    # The engine is reset to clear previous results.
    engine.reset()
    engine.problem_scores.clear()  # Previous problem scores are cleared.
    engine.remedies.clear()  # Previous remedies are cleared.
    
    # Each symptom is declared as a fact in the engine.
    for symptom in symptoms:
        engine.declare(Fact(symptom=symptom))
    
    # The rules are run to evaluate the symptoms.
    engine.run()

    # The output text area is cleared for new results.
    output_text.delete("1.0", tk.END)
    
    # The most likely issue is determined based on the highest score.
    if engine.problem_scores:
        most_likely_problem = max(engine.problem_scores, key=engine.problem_scores.get)
        remedy = engine.remedies[most_likely_problem]
        
        # The most likely issue and its suggested remedy are displayed.
        output_text.insert(tk.END, f"Most Likely Issue:\n- {most_likely_problem}\n")
        output_text.insert(tk.END, f"Suggested Remedy:\n- {remedy}\n")
    else:
        # A message is displayed if no issues are identified.
        output_text.insert(tk.END, "No issues identified. Check if symptoms are correctly entered.")

# The main application window is created.
root = tk.Tk()
root.title("Computer Troubleshooting System")

# A label is created for the input field with example text.
symptom_label = tk.Label(root, text="Enter symptoms (comma-separated):\nExample: Slow computer, High CPU usage")
symptom_label.pack(pady=(10,0))

# An entry field is created for user input.
symptom_entry = tk.Entry(root, width=50)
symptom_entry.pack(pady=(5,10))

# A button is created to trigger the diagnosis.
diagnose_button = tk.Button(root, text="Diagnose", command=diagnose)
diagnose_button.pack(pady=(0,10))

# A scrolled text area is created for displaying output.
output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=20)
output_text.pack()

# The main event loop is started to run the application.
root.mainloop()