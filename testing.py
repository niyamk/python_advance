from google.generativeai import GenerativeModel

# Replace 'YOUR_API_KEY' with your actual API key
api_key = "AIzaSyDvuE2YidoQDStDpuGgWlKxCAtbYq0mPMg"

# Choose the model (gemini-pro or gemini-pro-vision)
model_name = "gemini-pro"  # Or "gemini-pro-vision" for multimodal

# Create your prompt (text and/or images)
prompt = "Write a poem about a cat chasing a bird."

# Set desired token limits
max_input_tokens = 10000
max_output_tokens = 500

# Initialize the model with your API key
model = GenerativeModel(api_key)
model.generate_content
# Generate response with limits
response = model.generate(
    prompt=prompt,
    parameters={"maxTokens": max_output_tokens},
    max_tokens=max_input_tokens,
)

# Access and print the generated text
generated_text = response.text
print(f"Generated Text (limited to {max_output_tokens} tokens):\n{generated_text}")
