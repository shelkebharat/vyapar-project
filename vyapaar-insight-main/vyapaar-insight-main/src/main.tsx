import { createRoot } from "react-dom/client";
import App from "./App.tsx";
import "./index.css";

// Create the root element and render the App component
// The '!' tells TypeScript that the element exists and is not null
createRoot(document.getElementById("root")!).render(<App />);
