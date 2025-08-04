import React from "react";

// Exemplo de renderização de formulário dinâmico via MCP
export function MCPForm({ schema, onSubmit }: { schema: any; onSubmit: (values: any) => void }) {
  const [values, setValues] = React.useState({});

  function handleChange(name: string, val: any) {
    setValues((prev) => ({ ...prev, [name]: val }));
  }

  function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    onSubmit(values);
  }

  return (
    <form className="mb-4 p-4 border rounded shadow bg-white" onSubmit={handleSubmit}>
      <div className="font-bold mb-2">{schema.title || "Formulário"}</div>
      {schema.fields.map((f: any, i: number) => (
        <div key={i} className="mb-3">
          <label className="block mb-1 font-medium">{f.label}</label>
          {f.type === "text" && (
            <input
              type="text"
              value={values[f.name] || ""}
              onChange={e => handleChange(f.name, e.target.value)}
              className="border px-2 py-1 rounded w-full"
            />
          )}
          {f.type === "number" && (
            <input
              type="number"
              value={values[f.name] || ""}
              onChange={e => handleChange(f.name, e.target.value)}
              className="border px-2 py-1 rounded w-full"
            />
          )}
          {f.type === "select" && (
            <select
              value={values[f.name] || ""}
              onChange={e => handleChange(f.name, e.target.value)}
              className="border px-2 py-1 rounded w-full"
            >
              <option value="">Selecione...</option>
              {f.options.map((o: string, oi: number) => (
                <option key={oi} value={o}>{o}</option>
              ))}
            </select>
          )}
          {f.type === "toggle" && (
            <label className="flex items-center gap-2">
              <input
                type="checkbox"
                checked={!!values[f.name]}
                onChange={e => handleChange(f.name, e.target.checked)}
              />
              <span>{f.onLabel || "Sim"}</span>
            </label>
          )}
          {f.type === "date" && (
            <input
              type="date"
              value={values[f.name] || ""}
              onChange={e => handleChange(f.name, e.target.value)}
              className="border px-2 py-1 rounded w-full"
            />
          )}
        </div>
      ))}
      <button
        type="submit"
        className="bg-orange-500 text-white px-4 py-2 rounded font-bold mt-2"
      >
        Enviar
      </button>
    </form>
  );
}