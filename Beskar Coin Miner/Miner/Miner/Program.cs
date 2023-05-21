using Miner.Services;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
builder.Services.AddControllers();
builder.Services.AddSingleton<MiningService>();

var app = builder.Build();


app.MapControllers();

app.Run();
