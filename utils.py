from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from typing import List

class Models:
    """
    This hold all models available depending on the size
    """
    large = "microsoft/DialoGPT-large"
    medium = "microsoft/DialoGPT-medium"
    small = "microsoft/DialoGPT-small"



#You can change the model type here from small to medium or large I used small here because of bandwith I'll use to download the model
# the small model doesn't produce the best result so I'll advice you change it.
tokenizer = AutoTokenizer.from_pretrained(Models.medium)
model = AutoModelForCausalLM.from_pretrained(Models.medium)

def generate_response(msg_history, new_message:str ):
    """
    generate a response to a message based on the message sent and the message history

    Parameters
    ----------
    msg_history: 
        A list of tokenized conversation
    new_message, str:
        message to generate a response to.

    returns
    -------
        A tuple with a new message list with current message appended and the string response to that message.
    """
    encoded_message = tokenizer.encode(new_message + tokenizer.eos_token, return_tensors="pt")
    if msg_history is not None:
        new_msg_history = torch.cat([msg_history, encoded_message], dim=-1)
    else:
        new_msg_history = encoded_message

    output_tensor = model.generate(new_msg_history, max_length=1000, pad_token_id=tokenizer.eos_token_id)
    tokenized_output = tokenizer.decode(output_tensor[:, new_msg_history.shape[-1]:][0] , skip_special_tokens=True)

    return new_msg_history, tokenized_output
    
