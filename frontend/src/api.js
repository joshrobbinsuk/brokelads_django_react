import { fetchBaseQuery } from "@reduxjs/toolkit/query/react";
import { Auth } from "aws-amplify";

export const baseQuery = (baseUrl) =>
  fetchBaseQuery({
    baseUrl,
    prepareHeaders: async (headers) => {
      try {
        const session = await Auth.currentSession();
        const token = session.getIdToken().getJwtToken();
        headers.set("authorization", `Bearer ${token}`);
      } catch (err) {}
      return headers;
    },
  });
