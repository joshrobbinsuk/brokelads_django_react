const {
  REACT_APP_AWS_REGION,
  REACT_APP_COGNITO_CUSTOMER_APP_CLIENT_ID,
  REACT_APP_COGNITO_CUSTOMER_USER_POOL_ID,
  REACT_APP_API_ENDPOINT,
} = process.env;

const config = {
  api: {
    endpoint: REACT_APP_API_ENDPOINT,
    // websocket: REACT_APP_WEBSOCKET_ENDPOINT,
  },
  cognito: {
    customer: {
      region: REACT_APP_AWS_REGION,
      userPoolId: REACT_APP_COGNITO_CUSTOMER_USER_POOL_ID,
      userPoolWebClientId: REACT_APP_COGNITO_CUSTOMER_APP_CLIENT_ID,
    },
  },
  // peerConnection: {
  //   iceServers: [
  //     { urls: "stun:stun.stunprotocol.org:3478" },
  //     { urls: "stun:stun.l.google.com:19302" },
  //   ],
  // },
  // sentry: {
  //   dsn: REACT_APP_SENTRY_DSN,
  //   environment: REACT_APP_STAGE,
  // },
  // stage: REACT_APP_STAGE,
};

export default config;
