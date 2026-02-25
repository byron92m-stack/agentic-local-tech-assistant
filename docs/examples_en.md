# Usage Examples — Local Technical Agent

This document provides practical examples of how to interact with the **Local Technical Agent** through the `/chat` API endpoint.  
All examples assume the agent is running locally via:

```
python -m uvicorn agent.api.main:app --reload
```

and accessible at:

```
http://localhost:8000
```

---

## 1. Basic Interaction

### **Example: Ask a technical question**

**Request**

```json
{
  "message": "Explain the difference between WSL1 and WSL2."
}
```

**Response (simplified)**

```json
{
  "response": "WSL2 uses a real Linux kernel with virtualization, offering higher compatibility..."
}
```

---

## 2. Architecture & Debugging Questions

### **Example: Ask for help debugging a WSL issue**

**Request**

```json
{
  "message": "WSL2 is consuming too much RAM. What should I check?"
}
```

**Response (simplified)**

```json
{
  "response": "Check the .wslconfig file, verify memory limits, inspect Vmmem usage..."
}
```

---

## 3. Step‑by‑Step Explanations

### **Example: Ask for a guided explanation**

**Request**

```json
{
  "message": "Give me a step-by-step guide to install FastAPI inside WSL."
}
```

**Response (simplified)**

```json
{
  "response": "1. Update packages. 2. Create a virtual environment. 3. Install FastAPI..."
}
```

---

## 4. Code‑Related Questions

### **Example: Ask for a code snippet**

**Request**

```json
{
  "message": "Show me a minimal FastAPI example with one GET endpoint."
}
```

**Response (simplified)**

```json
{
  "response": "from fastapi import FastAPI ..."
}
```

---

## 5. System Design Questions

### **Example: Ask for an architecture explanation**

**Request**

```json
{
  "message": "Explain how the Local Technical Agent processes a request internally."
}
```

**Response (simplified)**

```json
{
  "response": "The API receives the message, builds the prompt, sends it to the LLM..."
}
```

---

## 6. Troubleshooting Examples

### **Example: Python environment issues**

**Request**

```json
{
  "message": "pip is not recognized in PowerShell. What should I do?"
}
```

**Response (simplified)**

```json
{
  "response": "Check if Python is added to PATH, verify installation, try python -m pip..."
}
```

---

## 7. WSL & Windows Integration Examples

### **Example: Ask about WSL performance**

**Request**

```json
{
  "message": "How can I improve disk performance in WSL2?"
}
```

**Response (simplified)**

```json
{
  "response": "Use ext4 instead of NTFS, avoid cross-boundary operations, enable sparse files..."
}
```

---

## 8. Agent Behavior Examples

### **Example: Ask about the cognitive flow**

**Request**

```json
{
  "message": "How does the Orchestrator and Validator work together?"
}
```

**Response (simplified)**

```json
{
  "response": "The Orchestrator proposes a plan, the Validator reviews and corrects it..."
}
```

---

## 9. Error Handling Examples

### **Example: Ollama not running**

**Request**

```json
{
  "message": "Why am I getting an error connecting to the model?"
}
```

**Response (simplified)**

```json
{
  "response": "[ERROR] Could not connect to Ollama..."
}
```

---

## 10. Advanced Usage

### **Example: Ask for a multi-step plan**

**Request**

```json
{
  "message": "Give me a 5-step plan to migrate a Python project into WSL."
}
```

**Response (simplified)**

```json
{
  "response": "1. Create a WSL environment. 2. Move project files. 3. Recreate venv..."
}
```

---

These examples demonstrate how the Local Technical Agent responds to different types of queries, from simple explanations to complex technical workflows.
