type ClientStatus = "active" | "paused" | "archived";

type Client = {
  name: string;
  status: ClientStatus;
  createdAT: Date;
};
