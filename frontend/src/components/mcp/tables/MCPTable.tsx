import React from "react";

export function MCPTable({ title, columns, rows }: any) {
  return (
    <div className="mb-4">
      {title && <div className="font-bold mb-1">{title}</div>}
      <div className="overflow-x-auto">
        <table className="min-w-full border rounded shadow bg-white text-sm">
          <thead>
            <tr>
              {columns.map((c: string, i: number) => (
                <th key={i} className="px-3 py-2 font-bold bg-orange-50 border-b">
                  {c}
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
            {rows.map((row: any, i: number) => (
              <tr key={i} className="border-b">
                {columns.map((c: string, j: number) => (
                  <td key={j} className="px-3 py-2">
                    {row[c]}
                  </td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}