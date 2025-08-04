import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import { MainLayout } from "./components/layout/MainLayout";
import { ChatWindow } from "./components/chat/ChatWindow";
import Login from "./pages/Login";
import ResetPassword from "./pages/ResetPassword";

export default function App() {
  return (
    <Router>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/reset-password" element={<ResetPassword />} />
        {/* Homepage agora redireciona para login */}
        <Route path="/" element={<Navigate to="/login" replace />} />
        <Route
          path="/chat"
          element={
            <MainLayout>
              <ChatWindow />
            </MainLayout>
          }
        />
      </Routes>
    </Router>
  );
}