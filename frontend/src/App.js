import React from "react";
import CssBaseline from "@mui/material/CssBaseline";
import { ThemeProvider } from "@mui/material/styles";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { Provider } from "react-redux";
import { SnackbarProvider } from "notistack";

import { NotificationConfigurator } from "./hooks";
import HelpDeskRoute from "./auth/HelpDeskRoute";
import BookmakerRoute from "./auth/BookmakerRoute";
import createStore from "./createStore";
import { lightTheme } from "./ui/theme";

const store = createStore();

const App = () => (
  <Provider store={store}>
    <ThemeProvider theme={lightTheme}>
      <CssBaseline />
      <SnackbarProvider>
        <NotificationConfigurator />
        <Router>
          <Routes>
            <Route path="/*" element={<BookmakerRoute />} />
            <Route path="/helpdesk" element={<HelpDeskRoute />} />
          </Routes>
        </Router>
      </SnackbarProvider>
    </ThemeProvider>
  </Provider>
);

export default App;
