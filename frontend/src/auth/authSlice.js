import { createSlice } from "@reduxjs/toolkit";

export const initialState = {};

const SLICE_NAME = "auth";

const authSlice = createSlice({
  name: SLICE_NAME,
  initialState,
  reducers: {},
});

export default authSlice.reducer;
