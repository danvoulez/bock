import React from "react";

export function Topbar() {
  return (
    <header className="h-14 bg-white shadow flex items-center px-6">
      <div className="flex-1 font-semibold text-gray-700 text-lg">
        Minicontratos MCP
      </div>
      <div className="flex items-center gap-4">
        {/* Espaço para notificações, avatar, etc */}
        <span className="text-xs text-gray-500">Conectado</span>
      </div>
    </header>
  );
}