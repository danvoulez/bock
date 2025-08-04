import React from "react";

export function MCPVideo({ src, caption }: any) {
  return (
    <figure className="mb-3">
      <video controls className="w-full max-w-lg rounded shadow" poster="">
        <source src={src} type="video/mp4" />
        Seu navegador não suporta vídeo.
      </video>
      {caption && <figcaption className="text-xs text-gray-500 mt-1">{caption}</figcaption>}
    </figure>
  );
}