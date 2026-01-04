what if similar to lora, we pass in a batch of images through vit/clip/dino and then add smaller layers in between for temporal attention 

you know about lora right? the low rank adaptation.. It basically reduces the learnable weights and utilizes the existing learned weights and faster and lighter finetuning with lora weights..
So what if we combine the idea of gradient accumulation and lora ? 
What we do is:
1. we process a block of a video at a time from  a vit backbone, and 
2. for each transformer block, we can either add a parallel block which would perform attention across the batch dimension which is nothing but temporal  attention
3. We can also add a different positional encodings for temporal dimension 
4. then combine the features
5. Do the same again for 'x' batches so that 'x' video batches are processed and then do the gradient accumulation