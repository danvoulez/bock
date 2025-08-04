import React from "react";
import clsx from "clsx";

export function MCPCard({
  title,
  avatar,
  status,
  fields = [],
  actions = [],
  badges = [],
  timeline = []
}: any) {
  return (
    <div className="border rounded-xl shadow p-5 mb-3 bg-white max-w-lg">
      <div className="flex items-center gap-4 mb-2">
        {avatar && (
          <img src={avatar} alt="avatar" className="w-12 h-12 rounded-full border" />
        )}
        <div>
          <div className="font-bold text-lg">{title}</div>
          <div className="flex gap-2 mt-1">
            {badges.map((b: any, i: number) => (
              <span
                key={i}
                className={clsx(
                  "px-2 py-1 text-xs font-semibold rounded",
                  b.color === "green" && "bg-green-200 text-green-700",
                  b.color === "blue" && "bg-blue-200 text-blue-700",
                  b.color === "orange" && "bg-orange-200 text-orange-700",
                  b.color === "red" && "bg-red-200 text-red-700"
                )}
              >
                {b.value ? `${b.label}: ${b.value}` : b.label}
              </span>
            ))}
          </div>
        </div>
        {status && (
          <span
            className={clsx(
              "ml-auto px-2 py-1 rounded text-xs font-bold",
              status === "ativo" && "bg-green-100 text-green-700",
              status === "pendente" && "bg-orange-100 text-orange-700",
              status === "penalizado" && "bg-red-100 text-red-700"
            )}
          >
            {status}
          </span>
        )}
      </div>
      <div className="flex flex-wrap gap-x-4 gap-y-1 text-sm text-gray-700 mb-2">
        {fields.map((f: any, i: number) => (
          <div key={i} className="flex gap-1 items-center">
            {f.icon && <span>{f.icon}</span>}
            <span className="font-medium">{f.label}:</span> <span>{f.value}</span>
          </div>
        ))}
      </div>
      {timeline && timeline.length > 0 && (
        <div className="my-2">
          <div className="text-xs font-bold text-gray-400">Histórico</div>
          <ul className="ml-2 text-xs">
            {timeline.map((t: any, i: number) => (
              <li key={i}>
                {t.icon} <b>{t.label}</b> — {t.date}
              </li>
            ))}
          </ul>
        </div>
      )}
      <div className="flex gap-2 mt-2">
        {actions.map((a: any, i: number) => (
          <button
            key={i}
            className={clsx(
              "px-3 py-1 rounded font-bold shadow text-xs",
              a.style === "primary" && "bg-green-500 text-white",
              a.style === "warning" && "bg-orange-500 text-white",
              a.style === "ghost" && "bg-gray-200 text-gray-700"
            )}
            onClick={() => window.alert(`Ação: ${a.command}`)}
          >
            {a.label}
          </button>
        ))}
      </div>
    </div>
  );
}