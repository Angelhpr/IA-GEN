import type { Message } from "../../types/message";
interface ChatMessagesProps {
  messages: Message[];
}

export default function ChatMessages({ messages }: ChatMessagesProps) {
  console.log("6. Render ChatMessages:", messages);
  return (
    <div
      className="
        flex-1
        space-y-6
        overflow-y-auto
        p-6
      "
    >
      {messages.map((message, index) => (
        <div
          key={index}
          className={`flex ${
            message.role === "user" ? "justify-end" : "justify-start"
          }`}
        >
          <div
            className={`
        max-w-[85%]
        rounded-2xl
        px-5
        py-4
        ${
          message.role === "user"
            ? "rounded-tr-sm bg-cyan-500 text-slate-950"
            : "rounded-tl-sm bg-slate-800 text-slate-200"
        }
      `}
          >
            <p>{message.content}</p>
          </div>
        </div>
      ))}
    </div>
  );
}
