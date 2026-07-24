export default function TypingIndicator() {
  return (
    <div className="flex w-full justify-start">
      <div className="flex max-w-[92%] flex-col items-start gap-1.5 sm:max-w-[85%]">
        <span
          aria-hidden="true"
          className="
            px-1
            text-[10px]
            font-medium
            uppercase
            tracking-[0.14em]
            text-[#94A3B8]
          "
        >
          IA-GEN
        </span>

        <div
          aria-hidden="true"
          className="
            rounded-2xl
            rounded-bl-sm
            border
            border-white/5
            bg-white/5
            px-5
            py-4
            shadow-sm
          "
        >
          <div className="flex items-center gap-1.5">
            <span
              className="
                h-1.5
                w-1.5
                animate-bounce
                rounded-full
                bg-[#60A5FA]
                [animation-delay:-0.3s]
              "
            />

            <span
              className="
                h-1.5
                w-1.5
                animate-bounce
                rounded-full
                bg-[#818CF8]
                [animation-delay:-0.15s]
              "
            />

            <span
              className="
                h-1.5
                w-1.5
                animate-bounce
                rounded-full
                bg-[#A78BFA]
              "
            />
          </div>
        </div>
      </div>
    </div>
  );
}
