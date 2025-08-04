// Tipos de payload MCP aceitos pelo renderizador

export interface MCPCardPayload {
  component: "card";
  type?: string;
  title: string;
  avatar?: string;
  status?: string;
  fields?: Array<{ label: string; value: string; icon?: string }>;
  actions?: Array<{ label: string; command: string; style?: string }>;
  badges?: Array<{ label: string; value?: string; color?: string }>;
  timeline?: Array<{ label: string; date: string; icon?: string }>;
}

export interface MCPTablePayload {
  component: "table";
  title?: string;
  columns: string[];
  rows: Array<Record<string, string | number>>;
}

export interface MCPImagePayload {
  component: "image";
  src: string;
  alt?: string;
  caption?: string;
}

export interface MCPVideoPayload {
  component: "video";
  src: string;
  caption?: string;
}

export interface MCPFormPayload {
  component: "form";
  schema: {
    title?: string;
    fields: Array<{
      name: string;
      label: string;
      type: "text" | "number" | "select" | "toggle" | "date";
      options?: string[];
      onLabel?: string;
      offLabel?: string;
    }>;
  };
}