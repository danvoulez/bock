import React, { useState } from "react";
import { supabase } from "../../lib/supabase";

export function AuthForm() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [view, setView] = useState<"login" | "forgot" | "reset" | "success">("login");
  const [message, setMessage] = useState<string | null>(null);

  async function handleLogin(e: React.FormEvent) {
    e.preventDefault();
    setMessage(null);
    const { error } = await supabase.auth.signInWithPassword({ email, password });
    if (error) setMessage(error.message);
    else setMessage("Login realizado! Redirecionando...");
  }

  async function handleForgot(e: React.FormEvent) {
    e.preventDefault();
    setMessage(null);
    const { error } = await supabase.auth.resetPasswordForEmail(email, {
      redirectTo: window.location.origin + "/reset-password",
    });
    if (error) setMessage(error.message);
    else {
      setView("success");
      setMessage("Link de redefinição enviado! Verifique seu e-mail.");
    }
  }

  return (
    <div className="max-w-sm mx-auto bg-white border shadow rounded p-6 mt-10">
      {view === "login" && (
        <form onSubmit={handleLogin} className="flex flex-col gap-3">
          <h2 className="font-bold text-xl mb-2">Entrar</h2>
          <input
            className="border rounded px-2 py-1"
            placeholder="Seu e-mail"
            type="email"
            value={email}
            onChange={e => setEmail(e.target.value)}
            required
          />
          <input
            className="border rounded px-2 py-1"
            placeholder="Sua senha"
            type="password"
            value={password}
            onChange={e => setPassword(e.target.value)}
            required
          />
          <button className="bg-orange-500 text-white rounded py-2 font-bold">Entrar</button>
          <button
            className="text-xs text-blue-600 underline"
            type="button"
            onClick={() => setView("forgot")}
          >
            Esqueci minha senha
          </button>
          {message && <div className="text-red-600">{message}</div>}
        </form>
      )}
      {view === "forgot" && (
        <form onSubmit={handleForgot} className="flex flex-col gap-3">
          <h2 className="font-bold text-xl mb-2">Recuperar Senha</h2>
          <input
            className="border rounded px-2 py-1"
            placeholder="Seu e-mail"
            type="email"
            value={email}
            onChange={e => setEmail(e.target.value)}
            required
          />
          <button className="bg-blue-500 text-white rounded py-2 font-bold">Enviar link</button>
          <button
            className="text-xs text-gray-500 underline"
            type="button"
            onClick={() => setView("login")}
          >
            Voltar ao login
          </button>
          {message && <div className="text-red-600">{message}</div>}
        </form>
      )}
      {view === "success" && (
        <div className="flex flex-col gap-3 items-center">
          <h2 className="font-bold text-xl mb-2">Verifique seu e-mail</h2>
          <p>Enviamos um link para redefinir sua senha.</p>
          <button
            className="text-xs text-gray-500 underline"
            type="button"
            onClick={() => setView("login")}
          >
            Voltar ao login
          </button>
        </div>
      )}
    </div>
  );
}