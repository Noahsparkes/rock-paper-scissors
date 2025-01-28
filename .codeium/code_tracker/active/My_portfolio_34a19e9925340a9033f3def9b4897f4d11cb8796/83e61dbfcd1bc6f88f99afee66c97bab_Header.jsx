
T/Users/noah/Personal project 23'/My_portfolio/My_portfolio/src/components/Header.jsx�import React, { useState } from 'react';
//import ThemeToggle from './ThemeToggle';

const Header = () => {
  const [menuOpen, setMenuOpen] = useState(false);

  const toggleMenu = () => {
    setMenuOpen((prev) => !prev);
  };

  const closeMenu = () => {
    setMenuOpen(false);
  };

  return (
    <header className="bg-white dark:bg-gray-800">
      <nav
        className="mx-auto flex max-w-7xl items-center justify-between p-6 lg:px-8"
        aria-label="Global"
      >
        <div className="flex lg:flex-1">
          <a href="#" className="-m-1.5 p-1.5">
            <span className="sr-only">Noah Sparkes</span>
            <h1 className="h-8 w-auto">Noah Sparkes</h1>
          </a>
        </div>
        <div className="flex lg:hidden">
          <button
            type="button"
            className="-m-2.5 inline-flex items-center justify-center rounded-md p-2.5 text-gray-700 dark:text-white"
            onClick={toggleMenu}
          >
            <span className="sr-only">Open main menu</span>
            <svg
              className="h-6 w-6 "
              fill="none"
              viewBox="0 0 24 24"
              strokeWidth="1.5"
              stroke="currentColor"
              aria-hidden="true"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5"
              />
            </svg>
          </button>
        </div>
        <div className="hidden lg:flex lg:gap-x-12">
          <a href="#" className="text-sm font-semibold text-gray-900 dark:text-white">
            Home
          </a>
          <a href="#" className="text-sm font-semibold text-gray-900 dark:text-white">
            About
          </a>
          <a href="#" className="text-sm font-semibold text-gray-900 dark:text-white">
            Projects
          </a>
          <a href="#" className="text-sm font-semibold text-gray-900 dark:text-white">
            Contact
          </a>
        </div>
      </nav> 

      {/* Mobile menu */}
      {menuOpen && (
        <>
          {/* Overlay */}
          <div
            className="fixed inset-0 bg-black bg-opacity-50 z-10"
            onClick={closeMenu}
          ></div>

          {/* Sliding menu */}
          <div className="fixed inset-y-0 right-0 w-64 bg-white shadow-lg z-20 dark:bg-gray-800">
            <button
              type="button"
              className="absolute top-4 right-4 text-gray-700"
              onClick={closeMenu}
            >
              <span className="sr-only">Close menu</span>
              <svg
                className="h-6 w-6"
                fill="none"
                viewBox="0 0 24 24"
                strokeWidth="1.5"
                stroke="currentColor"
                aria-hidden="true"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  d="M6 18L18 6M6 6l12 12"
                />
              </svg>
            </button>
            <ul className="mt-12 space-y-4 p-4">
              <li>
                <a href="#" className="block text-gray-900 font-semibold dark:text-white">
                  Home
                </a>
              </li>
              <li>
                <a href="#" className="block text-gray-900 font-semibold dark:text-white">
                  About
                </a>
              </li>
              <li>
                <a href="#" className="block text-gray-900 font-semibold dark:text-white">
                  Projects
                </a>
              </li>
              <li>
                <a href="#" className="block text-gray-900 font-semibold dark:text-white">
                  Contact
                </a>
              </li>
            </ul>
          </div>
        </>
      )}
    </header>
  );
};

export default Header;
�"(34a19e9925340a9033f3def9b4897f4d11cb8796*-/Users/noah/Personal project 23'/My_portfolio2afile:///Users/noah/Personal%20project%2023%27/My_portfolio/My_portfolio/src/components/Header.jsx::file:///Users/noah/Personal%20project%2023%27/My_portfolio