param(
  [Parameter(Mandatory=$true)]
  [ValidateSet("codex", "claude", "both", "repo-codex", "repo-claude", "claude-plugin")]
  [string]$Target
)

$RootDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$SkillSrc = Join-Path $RootDir "skills/exam-construction"
$PluginSrc = Join-Path $RootDir "claude-plugin"

function Copy-Directory($src, $dest) {
  $parent = Split-Path -Parent $dest
  if (!(Test-Path $parent)) { New-Item -ItemType Directory -Path $parent -Force | Out-Null }
  if (Test-Path $dest) { Remove-Item $dest -Recurse -Force }
  Copy-Item $src $dest -Recurse
  Write-Host "Installed: $dest"
}

function Install-Codex {
  Copy-Directory $SkillSrc (Join-Path $HOME ".agents/skills/exam-construction")
}

function Install-Claude {
  Copy-Directory $SkillSrc (Join-Path $HOME ".claude/skills/exam-construction")
}

function Install-RepoCodex {
  Copy-Directory $SkillSrc (Join-Path (Get-Location) ".agents/skills/exam-construction")
}

function Install-RepoClaude {
  Copy-Directory $SkillSrc (Join-Path (Get-Location) ".claude/skills/exam-construction")
}

function Install-ClaudePlugin {
  Copy-Directory $PluginSrc (Join-Path $HOME ".claude/skills/exam-construction-plugin")
}

switch ($Target) {
  "codex" { Install-Codex }
  "claude" { Install-Claude }
  "both" { Install-Codex; Install-Claude }
  "repo-codex" { Install-RepoCodex }
  "repo-claude" { Install-RepoClaude }
  "claude-plugin" { Install-ClaudePlugin }
}
