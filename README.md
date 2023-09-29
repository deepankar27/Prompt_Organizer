# 🗂️➡️📝 Prompt Organizer

<p align="center">
  <img src="assets/organize_llama.jpg" width="500" height="500" alt="Prompt Organizer">
</p>

## Managing LLM Prompts with Ease.

In the realm of **Prompt Engineering**, managing multiple versions of prompts can become overwhelming. Individuals and teams often face challenges in tracking and organizing different types of prompts, leading to the possibility of missing out on some of the best ones.

The lack of a structured approach to manage prompts efficiently often makes it difficult to navigate through them, causing a significant impediment in the workflow. Understanding this persistent issue, we introduce an application that serves as a beacon of relief: The **Prompt Organizer**.

## Features of the Prompt Organizer Pro.
1. Task-Based Organization:
Users can organize prompts under different tasks (Summarization, Topic Discovery, Intent identification etc), allowing for a clear and categorized view of each prompt.

2. Prompt Versions Management:
Within each task, users can create and manage multiple versions of prompts, each with its unique set of parameters.

3. Difference Visualization:
Users can leverage the integrated 'Show Diff' feature to effortlessly visualize and compare differences, additions, or deletions between various prompt versions, highlighted for easy spotting.

4. Prompt Parameters Configuration:
Users can easily configure various parameters like temperature, top_p, max tokens, and threshold for each version of the prompt.

5. Status Tracking:
The app allows users to set and track the status of each prompt, aiding in prompt evaluation and optimization.

6. Commenting Feature:
Each prompt version has an associated comment box, allowing users to annotate important notes or information related to the prompt.

7. System Prompt Management:
Alongside user prompts, the app also enables the management of system prompts, each with its commenting feature.

8. Save and Download:
Users can save their progress and download the organized prompts in YAML format, facilitating easy sharing and storage.

9. YAML Integration for Developer Pipelines:
This application seamlessly facilitates developers by allowing the direct incorporation of YAML files into their development pipelines, making the development process more intuitive and less error-prone.

10. Single user app:
This application is currently designed for individual use, with plans for future upgrades to support multiple users.

<p align="center">
  <img src="assets/capture_1.jpeg" width="500" height="500" alt="Prompt Organizer">
</p>


## How the app works?

https://github.com/deepankar27/Prompt_Organizer/assets/3585068/17a7db22-81a2-4e82-968c-d6537b0c305f


## How to run the app?
Go to the "Prompt Organizer" folder and run:

```
python app.py
```

## How to use the YAML file?

### How to read prompt from yaml?
Load the yaml file using this method:
```
import yaml

def read_template():
	directory_path = "data.yaml"
	yaml_content = ''

	with open(directory_path, "r") as f:
		try:
			yaml_content = yaml.safe_load(f)
		except yaml.YAMLError as e:
			print(f"Error parsing {directory_path}: {e}")
	
	return yaml_content

```

### How to read prompts for a given task with its version from the YAML file?
```
def get_prompt(task, version):
    yaml_content = read_template()
    version = "version"+"_"+str(version)
    return yaml_content[task]['prompts']['version_1']["prompt"]
	
prompt = get_prompt("Intent",1)

```

### How to get parameters of given task with its version from the YAML file?
```
def get_parameters(task, version):

    yaml_content = read_template()
    version = "version"+"_"+str(version)
    temp = yaml_content[task]['prompts'][version]['temperature']
    top_p = yaml_content[task]['prompts'][version]['top_p']
    max_tokens = yaml_content[task]['prompts'][version]['max_tokens']
    threshold = yaml_content[task]['prompts'][version]['threshold']

    return {"temperature":temp, "top_p":top_p, "max_tokens":max_tokens, "threshold":threshold}

params = get_parameters('Intent',1)

```

### How to handle dynamic input value in prompt?

Inside the prompt use placeholders and replace them with right contents:

Example Prompt:
> I am giving you a passage and you have to find the most important intents which are having high discussion value. All the intents must be in string format and relevancy score must be in floats format.\n\nYour response must contain outputs in dictionary format, following are some examples: [{intents: Intent Score},{}].\nDo not add any explanations.\n\nPassage:\n\n **##placeholder_1##**

Replace the **##placeholder_1##** dynamically with the input passage.

```
passage_content = "Your passage data"
prompt_passage = get_prompt('Intent',1)
prompt_passage = prompt_passage.replace("##placeholder_1##", passage_content)
```

Use the helper.py file to use all these methods.

### How to make a OpenAI call with Prompt Manager helper file.

```
openai.api_key = 'your-api-key-here'

passage_content = "Your data"

prompt_passage = get_prompt("Intent", 1) # This will provide you the prompt for the specified version and task.
system_prompt = get_sysprompt("Intent", 1) # This will provide you the system prompt for the specified version and task.
prompt_param = get_parameters("Intent", 1) # This will provide you the all parameters for the specified version and task.

prompt_passage = prompt_passage.replace("##placeholder_1##", passage_content)

response = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
	temperature = prompt_param["temperature"],
    top_p = prompt_param["top_p"],
    max_tokens = prompt_param["max_tokens"],
    messages=[
        {"role": "system", "content": prompt_passage},
        {"role": "user", "content": system_prompt},
    ]
)

# Extracting response
answer = response['choices'][0]['message']['content']
print(answer)
```

## Future ideas 💡
1. Setup git integration.
2. Design for multi-user use.
3. Integration of data and OpenAI/ Custom LLM APIs for auto evaluation.
4. Need to evaluate possibility of integrations with MLops.

All with ease of use.

## 🌟 Special Acknowledgments: Powered by ChatGPT 🌟

In the creation of the **Prompt Organizer**, a revolutionary entity has played an instrumental role, serving as the backbone of the development process – **ChatGPT by OpenAI**. I haven't written a single line of code! I wanted to give a try how well it can help me in the development cycle, and here it is - the well-tested, user friendly
:clap: :clap: **Prompt Organizer!** :clap: :clap:
