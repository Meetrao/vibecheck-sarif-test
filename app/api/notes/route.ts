import { db } from "../../../lib/db";

const headers = { "Access-Control-Allow-Origin": "*" };

export async function POST(req: Request) {
  const { id, text } = await req.json();
  await db.query(`update notes set text = '${text}' where id = ${id}`);
  return Response.json({ ok: true }, { headers });
}
