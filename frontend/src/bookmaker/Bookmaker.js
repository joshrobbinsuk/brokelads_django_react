import React from "react";
import { Container } from "@mui/material";
import { Routes, Route } from "react-router-dom";
import { useDispatch } from "react-redux";

import Nav from "src/ui/Nav";
import NextMatches from "./nextMatches/NextMatches";
import MyBets from "./myBets/MyBets";
import MyAccount from "./account/Account";
import bookmakerApi from "./bookmakerApi";

const Bookmaker = ({ signOut }) => {
  // clears api
  const dispatch = useDispatch();
  dispatch(bookmakerApi.util.resetApiState());

  return (
    <>
      {/* hover color + more */}
      <Nav />
      <Container>
        <Routes>
          <Route path="bets" element={<MyBets />} />
          <Route
            path="account"
            element={<MyAccount handleLogout={() => signOut()} />}
          />
          <Route path="*" element={<NextMatches />} />
        </Routes>
      </Container>
    </>
  );
};

export default Bookmaker;
