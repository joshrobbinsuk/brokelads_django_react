import { useSnackbar } from "notistack";
import { useCallback } from "react";

const defaultError = "Ooops there was an error doing that";
export const useNotification = () => {
  const { enqueueSnackbar } = useSnackbar();

  const showError = useCallback(
    (message, options = {}) => {
      enqueueSnackbar(message || defaultError, {
        variant: "error",
        ...options,
      });
    },
    [enqueueSnackbar],
  );
  const showSuccess = useCallback(
    (message, options = {}) => {
      enqueueSnackbar(message, { variant: "success", ...options });
    },
    [enqueueSnackbar],
  );

  return {
    showSuccess,
    showError,
  };
};

// Allow notifications outside of components
let snackbarRef;
export const NotificationConfigurator = () => {
  snackbarRef = useSnackbar();
  return null;
};

export const notificationActions = {
  showSuccess(msg) {
    snackbarRef.enqueueSnackbar(msg, { variant: "success" });
  },
  showError(msg) {
    snackbarRef.enqueueSnackbar(msg || defaultError, {
      variant: "error",
    });
  },
};
