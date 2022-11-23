import { configureStore } from "@reduxjs/toolkit";
import { combineReducers } from "redux";

import auth from "./auth/authSlice";
import bookmaker from "./bookmaker/bookmakerSlice";
import bookmakerApi from "./bookmaker/bookmakerApi";

const rootReducer = combineReducers({
  auth,
  bookmaker,
  [bookmakerApi.reducerPath]: bookmakerApi.reducer,
});

const createStore = () => {
  const store = configureStore({
    reducer: rootReducer,
    middleware: (getDefaultMiddleware) =>
      getDefaultMiddleware().concat(bookmakerApi.middleware),
    devTools: process.env.NODE_ENV !== "production",
  });
  return store;
};

export default createStore;
