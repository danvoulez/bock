import React from "react";

export function MCPImage({ src, alt, caption }: any) {
  return (
    <figure className="mb-3">
      <img src={src} alt={alt || "imagem"} className="rounded shadow max-h-80" />
      {caption && <figcaption className="text-xs text-gray-500 mt-1">{caption}</figcaption>}
    </figure>
  );
}