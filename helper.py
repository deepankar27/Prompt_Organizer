import yaml
import os

#This can be loaded from configs or hardcode the path or pass as a
# variable to read_template method it is upto you.

yaml_dir_path = ""

def read_template():
    '''
        This method will read the yaml file from your dir path
    '''
    directory_path = yaml_dir_path
    yaml_content = ''

    with open(directory_path, "r") as f:
        try:
            yaml_content = yaml.safe_load(f)
        except yaml.YAMLError as e:
            print(f"Error parsing {directory_path}: {e}")
    
    return yaml_content


def get_prompt(task, version):
    '''
        This method will return you the prompt for the given task

        input:
        task (str): name of the task like intent, summary, topic discovery etc
        version (int): version of the prompt
        return (str):
        prompt
    '''
    yaml_content = read_template()
    version = "version"+"_"+str(version)
    return yaml_content[task]['prompts'][version]["prompt"]


def get_sysprompt(task, version):
    '''
        This method will return you the system prompt for the given task

        input:
        task (str): name of the task like intent, summary, topic discovery etc
        version (int): version of the prompt
        return (str):
        system prompt
    '''
    yaml_content = read_template()
    version = "version"+"_"+str(version)
    return yaml_content[task]['system_prompts'][version]["prompt"]

def get_parameters(task, version):
    '''
        This method will provide you the parameters of the given task
        input:
        task (str): name of the task like intent, summary, topic discovery etc
        version (int): version of the prompt
        return (dict):
        it will return you the parameters in dict format
    '''

    yaml_content = read_template()
    version = "version"+"_"+str(version)

    if yaml_content[task]['prompts'][version]['temperature'] != '':
        temp = float(yaml_content[task]['prompts'][version]['temperature'])
    else: temp = 0.0

    if yaml_content[task]['prompts'][version]['top_p'] != '':
        top_p = float(yaml_content[task]['prompts'][version]['top_p'])
    else: top_p = 0.0
    
    if yaml_content[task]['prompts'][version]['max_tokens'] != '':
        max_tokens = int(yaml_content[task]['prompts'][version]['max_tokens'])
    else: max_tokens = 0

    if yaml_content[task]['prompts'][version]['threshold'] != '':
        threshold = float(yaml_content[task]['prompts'][version]['threshold'])
    else: threshold = 0.0

    return {"temperature":temp, "top_p":top_p, "max_tokens":max_tokens, "threshold":threshold}


