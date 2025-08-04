import React from "react";
import { ChatHistorySidebar } from "../chat/ChatHistorySidebar";

const navItems = [
  { label: "Chat", icon: "💬" },
  { label: "Ideias", icon: "💡" },
  { label: "Contratos", icon: "📄" },
  { label: "Pessoas", icon: "🧑‍🤝‍🧑" },
  { label: "Objetos", icon: "📦" },
  { label: "Governança", icon: "🏛️" },
];

export function Sidebar() {
  return (
    <aside className="w-64 bg-white border-r h-full flex flex-col py-4">
      <div className="text-2xl font-bold text-orange-500 px-6 mb-6">Minicontratos</div>
      <nav className="flex flex-col gap-2 flex-none mb-6">
        {navItems.map((item) => (
          <div key={item.label}
            className="px-6 py-2 rounded hover:bg-orange-50 transition flex items-center gap-3 cursor-pointer">
            <span>{item.icon}</span> {item.label}
          </div>
        ))}
      </nav>
      <div className="flex-1 overflow-y-auto">
        <ChatHistorySidebar />
      </div>
      <div className="px-6 text-xs text-gray-400 mt-4">v1.0.0</div>
    </aside>
  );
}