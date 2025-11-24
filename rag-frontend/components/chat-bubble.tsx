// components/chat-bubble.tsx

interface ChatBubbleProps {
  role: "user" | "assistant";
  message: string;
}

export function ChatBubble({ role, message }: ChatBubbleProps) {
  const isUser = role === "user";

  return (
    <div
      className={`w-full flex mb-3 ${isUser ? "justify-end" : "justify-start"}`}
    >
      <div
        className={`max-w-[75%] rounded-lg px-4 py-2 text-sm ${
          isUser ? "bg-blue-600 text-white" : "bg-gray-200 text-gray-900"
        }`}
      >
        {message}
      </div>
    </div>
  );
}
