
Z/Users/noah/Personal project 23'/My_portfolio/My_portfolio/src/components/CustomCursor.jsxÂimport React, { useEffect } from "react";

const CustomCursor = () => {
  useEffect(() => {
    // Prevent duplicate cursors
    if (!window.kursorInstance) {
      // Check if dark mode is enabled
      const isDarkMode = window.matchMedia("(prefers-color-scheme: dark)").matches;

      // Initialize the Kursor instance with the appropriate color
      window.kursorInstance = new kursor({
        type: 4,
        color: isDarkMode ? "#fff" : "#000", // White for dark mode, black for light mode
      });
    }
  }, []);

  return null; 
};

export default CustomCursor;


À 
ÀÂ "(34a19e9925340a9033f3def9b4897f4d11cb8796*-/Users/noah/Personal project 23'/My_portfolio2gfile:///Users/noah/Personal%20project%2023%27/My_portfolio/My_portfolio/src/components/CustomCursor.jsx::file:///Users/noah/Personal%20project%2023%27/My_portfolio