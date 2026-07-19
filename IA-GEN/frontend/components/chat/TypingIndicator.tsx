export default function TypingIndicator() {
  return (
    <div className="flex justify-start">
      <div
        className="
          rounded-2xl
          rounded-tl-sm
          bg-slate-800
          px-5
          py-4
        "
      >
        <div className="flex items-center gap-1.5">
          <span
            className="
              h-1.5
              w-1.5
              animate-bounce
              rounded-full
              bg-slate-300
              [animation-delay:-0.3s]
            "
          />

          <span
            className="
              h-1.5
              w-1.5
              animate-bounce
              rounded-full
              bg-slate-300
              [animation-delay:-0.15s]
            "
          />

          <span
            className="
              h-1.5
              w-1.5
              animate-bounce
              rounded-full
              bg-slate-300
            "
          />
        </div>
      </div>
    </div>
  );
}
