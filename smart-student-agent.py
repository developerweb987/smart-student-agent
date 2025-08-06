import google.generativeai as genai

genai.configure(api_key="AIzaSyA5cXSAj9Eq9K8eCKrfKMoSoX5fVyXXqbA")  

model = genai.GenerativeModel(model_name="gemini-1.5-flash")

class SmartStudentAgent:
    def __init__(self, model):
        self.model = model

    def generate(self, prompt):
        try:
            response = self.model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            return f"Error: {e}"

    def answer_academic_question(self, question):
        prompt = f"Answer this academic question in a simple and clear way:\n\n{question}"
        return self.generate(prompt)

    def provide_study_tips(self, topic):
        prompt = f"Give 3 practical and effective study tips for the topic:\n\n{topic}"
        return self.generate(prompt)

    def summarize_passage(self, text):
        prompt = f"Summarize the following passage in 2-3 simple lines:\n\n{text}"
        return self.generate(prompt)

def main():
    agent = SmartStudentAgent(model)

    print("Welcome to Smart Student Agent Assistant")
    print("1. Academic Question")
    print("2. Study Tips")
    print("3. Summarize Passage")
    choice = input("Choose an option (1-3): ")

    if choice == "1":
        question = input("Enter your academic question: ")
        print(agent.answer_academic_question(question))
    elif choice == "2":
        topic = input("Enter the study topic: ")
        print(agent.provide_study_tips(topic))
    elif choice == "3":
        passage = input("Paste the text to summarize: ")
        print(agent.summarize_passage(passage))
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
