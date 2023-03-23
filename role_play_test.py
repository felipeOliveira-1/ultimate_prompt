import openai

# Set up the OpenAI API key
openai.api_key = ""


def generate_roleplay_response(subject):
    # Initial roleplay prompt
    initial_prompt = f"Hey AI, let's roleplay that I am the AI, and you are the user. Make a request using a perfect prompt to know more about {subject}."

    # Generate the perfect prompt request using GPT-3.5 Turbo
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": initial_prompt},
        ]
    )

    # Extract the perfect prompt from the response
    perfect_prompt = response["choices"][0]["message"]["content"]
    
    # Print the perfect prompt
    print(f"\nPerfect prompt: {perfect_prompt}")

    # Change the roleplay and generate the response to the perfect prompt
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": perfect_prompt},
        ]
    )

    # Extract the answer to the perfect prompt
    answer = response["choices"][0]["message"]["content"]

    return answer

if __name__ == "__main__":
    # Get user input for the subject
    user_subject = input("\nEnter a subject: ")
    
    # Generate the roleplay response based on the user input
    roleplay_answer = generate_roleplay_response(user_subject)
    
    # Print the final answer
    print(roleplay_answer)
