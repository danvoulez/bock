import React from "react";
import { MCPCard } from "./cards/MCPCard";
import { MCPTable } from "./tables/MCPTable";
import { MCPImage } from "./media/MCPImage";
import { MCPVideo } from "./media/MCPVideo";

export function MCPRenderer({ payload }: { payload: any }) {
  if (!payload) return null;
  switch (payload.component) {
    case "card":
      return <MCPCard {...payload} />;
    case "table":
      return <MCPTable {...payload} />;
    case "image":
      return <MCPImage {...payload} />;
    case "video":
      return <MCPVideo {...payload} />;
    default:
      return <pre className="text-xs text-gray-600">{JSON.stringify(payload, null, 2)}</pre>;
  }
}