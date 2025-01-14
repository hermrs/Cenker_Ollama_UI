import tkinter as tk
from tkinter import scrolledtext
import threading
from ollama import generate

conversation_history = []

def build_prompt_from_history() -> str:
   
    prompt_parts = []
    for msg in conversation_history:
        role = msg["role"]
        content = msg["content"]
        if role == "user":
            prompt_parts.append(f"User: {content}")
        else:
            prompt_parts.append(f"Assistant: {content}")
    return "\n".join(prompt_parts) + "\n\nAssistant:"

def get_ollama_response(prompt: str, use_stream: bool = False) -> str:
    
    response_text = ""
    print(f"\n[DEBUG] Calling generate(...) with stream={use_stream}")
    for chunk in generate(model="llama3.2:latest", prompt=prompt, stream=use_stream):
        print("[DEBUG] Chunk received:", chunk)
        
       e
        if isinstance(chunk, tuple) and len(chunk) == 2:
            key, value = chunk
            
            if key in ("data", "response"):
                response_text += value
        else:
            print("[DEBUG] Unknown chunk format:", chunk)
    
    print("[DEBUG] Final response_text so far:", response_text)
    return response_text.strip()

def send_message():
   
    user_text = user_entry.get("1.0", 'end-1c').strip()
    if not user_text:
        return
    
    conversation_history.append({"role": "user", "content": user_text})

    chat_display.configure(state='normal')
    chat_display.insert(tk.END, f"User:\n{user_text}\n\n")
    chat_display.configure(state='disabled')
    user_entry.delete("1.0", tk.END)

    def background_ollama():
        prompt_text = build_prompt_from_history()

       
        response_text = get_ollama_response(prompt_text, use_stream=False)
        

        conversation_history.append({"role": "assistant", "content": response_text})

        chat_display.configure(state='normal')
        chat_display.insert(tk.END, f"Assistant:\n{response_text}\n\n")
        chat_display.configure(state='disabled')
        chat_display.see(tk.END)

    t = threading.Thread(target=background_ollama, daemon=True)
    t.start()


root = tk.Tk()
root.title("Cenker_llma_UI (capture 'response')")

chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20, state='disabled')
chat_display.pack(padx=10, pady=10)

user_entry = tk.Text(root, height=3, wrap=tk.WORD)
user_entry.pack(padx=10, fill='x')

send_button = tk.Button(root, text="Gönder", command=send_message)
send_button.pack(pady=5)

root.mainloop()

