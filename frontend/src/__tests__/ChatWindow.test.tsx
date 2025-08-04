import { render, screen, fireEvent } from "@testing-library/react";
import { ChatWindow } from "../components/chat/ChatWindow";

test("renders ChatWindow and sends message", () => {
  render(<ChatWindow />);
  const input = screen.getByPlaceholderText("Digite sua mensagem...");
  fireEvent.change(input, { target: { value: "contrato" } });
  fireEvent.submit(input.closest("form")!);
  expect(screen.getByText(/Contrato de Manutenção/)).toBeInTheDocument();
});