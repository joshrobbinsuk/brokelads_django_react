import React, { useState } from "react";
import {
  Dialog,
  DialogContent,
  DialogTitle,
  DialogActions,
  Button,
} from "@mui/material";
import * as yup from "yup";
import { Formik } from "formik";
import { useNavigate } from "react-router-dom";

import { useNotification } from "src/hooks";

import { Loading, Error } from "src/ui";
import BetFormContent from "./BetFormContent";
import { usePostBetMutation, useFetchUserQuery } from "../bookmakerApi";

const BetDialog = ({ trigger, choice, text, odds, matchId }) => {
  const { data, isLoading, isError } = useFetchUserQuery();

  const [betStaged, setBetStaged] = useState(false);
  const [modalOpen, setModalOpen] = useState(false);
  const handleShowModal = () => setModalOpen(true);
  const handleCloseModal = () => {
    setModalOpen(false);
    setBetStaged(false);
  };

  const navigate = useNavigate();
  const { showError, showSuccess } = useNotification();
  const [postBet] = usePostBetMutation();

  if (isLoading) {
    return <Loading />;
  }
  if (isError) {
    return <Error />;
  }
  const { balance } = data;

  const validationSchema = yup.object().shape({
    matchId: yup.string().required(),
    choice: yup.string().required(),
    stake: yup.number().required().positive().max(balance),
  });

  const initialValues = {
    matchId,
    choice,
    stake: 0,
    returns: 0,
  };

  const handleSubmit = async (values) => {
    try {
      await postBet(values).unwrap();
      handleCloseModal();
      navigate("bets");
      showSuccess("Your bet has been made. Good luck!");
    } catch (e) {
      showError(e.data?.error);
    }
  };
  return (
    <>
      {trigger({ onClick: handleShowModal })}
      <Dialog open={modalOpen} onClose={handleCloseModal}>
        <DialogTitle sx={{ mb: 0 }}>{text}</DialogTitle>
        <Formik
          initialValues={initialValues}
          onSubmit={handleSubmit}
          validationSchema={validationSchema}
        >
          {({ handleSubmit, isValid, errors }) => {
            if (errors.stake) {
              setBetStaged(false);
            }
            return (
              <>
                <DialogContent>
                  <BetFormContent odds={odds} balance={balance} />
                </DialogContent>
                <DialogActions
                  sx={{
                    display: "flex",
                    flexDirection: "row",
                    justifyContent: "flex-start",
                    width: "100%",
                  }}
                >
                  <Button
                    onClick={() => setBetStaged(true)}
                    disabled={!isValid}
                  >
                    Place Bet
                  </Button>
                  <Button
                    sx={{ display: betStaged ? "flex" : "none" }}
                    onClick={handleSubmit}
                  >
                    Confirm Bet
                  </Button>
                </DialogActions>
              </>
            );
          }}
        </Formik>
      </Dialog>
    </>
  );
};

export default BetDialog;
