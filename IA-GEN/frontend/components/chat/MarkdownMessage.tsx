import ReactMarkdown, { type Components } from "react-markdown";
import remarkGfm from "remark-gfm";

interface MarkdownMessageProps {
  content: string;
}

const markdownComponents: Components = {
  p: ({ children }) => <p className="mb-3 leading-6 last:mb-0">{children}</p>,

  strong: ({ children }) => (
    <strong className="font-semibold text-white">{children}</strong>
  ),

  em: ({ children }) => <em className="text-slate-200">{children}</em>,

  h1: ({ children }) => (
    <h1 className="mb-3 mt-4 text-lg font-semibold text-white first:mt-0">
      {children}
    </h1>
  ),

  h2: ({ children }) => (
    <h2 className="mb-2 mt-4 text-base font-semibold text-white first:mt-0">
      {children}
    </h2>
  ),

  h3: ({ children }) => (
    <h3 className="mb-2 mt-3 text-sm font-semibold text-white first:mt-0">
      {children}
    </h3>
  ),

  ul: ({ children }) => (
    <ul className="mb-3 ml-5 list-disc space-y-1.5 marker:text-[#60A5FA] last:mb-0">
      {children}
    </ul>
  ),

  ol: ({ children }) => (
    <ol className="mb-3 ml-5 list-decimal space-y-1.5 marker:font-medium marker:text-[#60A5FA] last:mb-0">
      {children}
    </ol>
  ),

  li: ({ children }) => <li className="pl-1 leading-6">{children}</li>,

  blockquote: ({ children }) => (
    <blockquote className="my-3 border-l-2 border-[#60A5FA] pl-4 text-slate-300">
      {children}
    </blockquote>
  ),

  pre: ({ children }) => (
    <pre className="my-3 overflow-x-auto rounded-xl border border-white/10 bg-[#020617]/80 p-4 text-left">
      {children}
    </pre>
  ),

  code: ({ className, children }) => {
    const rawValue = String(children);
    const isBlockCode =
      Boolean(className?.startsWith("language-")) || rawValue.includes("\n");

    const value = rawValue.replace(/\n$/, "");

    if (isBlockCode) {
      return (
        <code
          className={`${className ?? ""} block font-mono text-[13px] leading-6 text-slate-100`}
        >
          {value}
        </code>
      );
    }

    return (
      <code className="rounded-md border border-white/10 bg-black/30 px-1.5 py-0.5 font-mono text-[0.88em] text-[#93C5FD]">
        {children}
      </code>
    );
  },

  a: ({ href, children }) => (
    <a
      href={href}
      target="_blank"
      rel="noopener noreferrer"
      className="font-medium text-[#60A5FA] underline decoration-[#60A5FA]/40 underline-offset-2 transition hover:text-[#93C5FD]"
    >
      {children}
    </a>
  ),

  img: () => null,

  hr: () => <hr className="my-4 border-white/10" />,

  table: ({ children }) => (
    <div className="my-3 overflow-x-auto">
      <table className="min-w-full border-collapse text-left text-sm">
        {children}
      </table>
    </div>
  ),

  th: ({ children }) => (
    <th className="border border-white/10 bg-white/5 px-3 py-2 font-semibold text-white">
      {children}
    </th>
  ),

  td: ({ children }) => (
    <td className="border border-white/10 px-3 py-2 text-slate-300">
      {children}
    </td>
  ),
};

export default function MarkdownMessage({ content }: MarkdownMessageProps) {
  return (
    <div className="min-w-0 wrap-break-word">
      <ReactMarkdown
        skipHtml
        remarkPlugins={[remarkGfm]}
        components={markdownComponents}
      >
        {content}
      </ReactMarkdown>
    </div>
  );
}
