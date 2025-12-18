"use client";

import { useState } from "react";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { ScrollArea } from "@/components/ui/scroll-area";
import { ChatBubble } from "@/components/chat-bubble";

export default function ChatPage() {
  const [messages, setMessages] = useState<
    { role: "user" | "assistant"; content: string }[]
  >([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  async function sendMessage() {
    // if (!input.trim()) return;
    const question = input.trim();
    if (!question) return;

    // Add user message instantly
    const newMessages = [
      ...messages,
      { role: "user" as const, content: question },
    ];
    setMessages(newMessages);
    setInput("");
    setLoading(true);

    // Call backend /ask endpoint
    try {
      const res = await fetch(
        "http://localhost:8000/ask?question=" + encodeURIComponent(question),
        {
          method: "POST",
        }
      );

      const data = await res.json();

      // Add assistant reply
      setMessages([
        ...newMessages,
        { role: "assistant", content: data.answer || "No answer received." },
      ]);
    } catch (error) {
      setMessages([
        ...newMessages,
        { role: "assistant", content: "Error talking to backend." },
      ]);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="flex flex-col h-screen p-4">
      {/* Chat history */}
      <ScrollArea className="flex-1 border rounded-md p-4 mb-4">
        {messages.map((m, i) => (
          <ChatBubble key={i} role={m.role} message={m.content} />
        ))}

        {loading && <ChatBubble role="assistant" message="Thinking..." />}
      </ScrollArea>

      {/* Input bar */}
      <div className="flex gap-2">
        <Input
          placeholder="Ask something..."
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && sendMessage()}
        />
        <Button onClick={sendMessage}>Send</Button>
      </div>
    </div>
  );
}
