import React, { useState } from "react";
import { supabase } from "../../lib/supabase";

export function ResetPasswordForm() {
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState<string | null>(null);

  async function handleReset(e: React.FormEvent) {
    e.preventDefault();
    setMessage(null);
    const { error } = await supabase.auth.updateUser({ password });
    if (error) setMessage(error.message);
    else setMessage("Senha redefinida com sucesso! Faça login.");
  }

  return (
    <div className="max-w-sm mx-auto bg-white border shadow rounded p-6 mt-10">
      <form onSubmit={handleReset} className="flex flex-col gap-3">
        <h2 className="font-bold text-xl mb-2">Redefinir Senha</h2>
        <input
          className="border rounded px-2 py-1"
          placeholder="Nova senha"
          type="password"
          value={password}
          onChange={e => setPassword(e.target.value)}
          required
        />
        <button className="bg-green-600 text-white rounded py-2 font-bold">Salvar Nova Senha</button>
        {message && <div className="text-green-600">{message}</div>}
      </form>
    </div>
  );
}