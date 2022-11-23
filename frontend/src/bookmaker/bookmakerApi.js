import { createApi } from "@reduxjs/toolkit/query/react";

import { baseQuery } from "src/api";
import config from "src/config";

export const FETCH_MY_BETS_LIMIT = 5;

const bookmakerApi = createApi({
  reducerPath: "bookmakerApi",
  baseQuery: baseQuery(`${config.api.endpoint}/bookmaker`),
  tagTypes: ["MY_BETS", "USER"],
  endpoints: (builder) => ({
    fetchUser: builder.query({
      query: () => ({
        url: "/get-customer/",
      }),
      providesTags: ["USER"],
    }),
    fetchNextMatches: builder.query({
      query: () => ({
        url: "/next-matches/",
      }),
    }),

    fetchMyBets: builder.query({
      query: ({ ordering, page, outcome }) => {
        const limit = FETCH_MY_BETS_LIMIT;
        const offset = page * limit;
        const params = {
          ordering,
          outcome,
          offset,
          limit,
        };
        return {
          url: "/my-bets/",
          params,
        };
      },
      providesTags: ["MY_BETS"],
    }),

    postBet: builder.mutation({
      query: (params) => ({
        url: "/my-bets/",
        body: params,
        method: "POST",
      }),
      invalidatesTags: ["MY_BETS", "USER"],
    }),

    fetchServerWillRefresh: builder.query({
      query: (params) => ({
        url: "/server-will-refresh/",
        params: params,
      }),
    }),
  }),
});

export const {
  useFetchUserQuery,
  useLazyFetchUserQuery,
  useFetchNextMatchesQuery,
  usePostBetMutation,
  useFetchMyBetsQuery,
  useLazyFetchMyBetsQuery,
  useFetchServerWillRefreshQuery,
  useLazyFetchServerWillRefreshQuery,
} = bookmakerApi;

export default bookmakerApi;
