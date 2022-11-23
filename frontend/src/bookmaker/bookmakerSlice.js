import { createSlice } from "@reduxjs/toolkit";

export const initialState = {
  myBets: {
    page: 0,
    outcome: "UNDECIDED",
    ordering: "match__datetime",
  },
};

const SLICE_NAME = "bookmaker";

const bookmakerSlice = createSlice({
  name: SLICE_NAME,
  initialState,
  reducers: {
    setMyBetsOutcome: (state, { payload }) => {
      state.myBets.outcome = payload;
    },
    setMyBetsOrdering: (state, { payload }) => {
      state.myBets.ordering = payload;
    },
    setMyBetsPage: (state, { payload }) => {
      state.myBets.page = payload;
    },
  },
});

export const { setMyBetsOrdering, setMyBetsPage, setMyBetsOutcome } =
  bookmakerSlice.actions;

export const selectMyBetsOrdering = (state) => state.bookmaker.myBets.ordering;
export const selectMyBetsPage = (state) => state.bookmaker.myBets.page;
export const selectMyBetsOutcome = (state) => state.bookmaker.myBets.outcome;
export default bookmakerSlice.reducer;
